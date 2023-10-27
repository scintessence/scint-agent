import json
import importlib
from typing import Dict, List, Any


from services.logger import log
from services.openai import completion
from core.config import GPT4, INTERFACE_INIT, INTERFACE_FUNC, INTERFACE_CONFIG
from core.message import Message
from core.agent import Agent


class ChatInterface(Agent):
    def __init__(self):
        log.info(f"Initializing Scint interface.")

        self.name = "interface"
        self.system_init: Dict[str, str] = INTERFACE_INIT
        self.function: Dict[str, Any] = INTERFACE_FUNC
        self.config: Dict[str, Any] = INTERFACE_CONFIG
        self.messages: List[Dict[str, str]] = [self.system_init]

    async def process_request(self, payload):
        log.info(f"Processing request.")
        self.payload: Message = payload
        self.messages.append(payload.message_data)
        state = await self.state()
        res = await completion(**state)
        res_message = res["choices"][0].get("message")  # type: ignore

        if not isinstance(res_message, dict):
            log.error("res_message is not a dictionary.")
            return

        content = res_message.get("content")
        function_call = res_message.get("function_call")

        if content is not None:
            reply = await self.generate_reply(res_message)
            return reply

        elif function_call is not None:
            new_request = await self.eval_function_call(res_message)  # type: ignore

            if new_request:
                return await self.process_request(new_request)

            else:
                log.error("Function call did not return a valid request.")
                return

    async def eval_function_call(self, res_message):
        log.info("Evaluating worker function call.")

        function_call = res_message.get("function_call")
        function_name = function_call.get("name")
        function_args = function_call.get("arguments")

        if isinstance(function_args, str):
            function_args = json.loads(function_args)

        if function_name.strip() == self.function.get("name"):
            module_name = "handlers.weather"
            module = importlib.import_module(module_name)
            method_to_call = getattr(module, function_name, None)

            if method_to_call:
                try:
                    result = await method_to_call(**function_args)
                    result_message = Message(self.name, "Interface", result)
                    return result_message

                except Exception as e:
                    log.error(f"Error during function call: {e}")
            else:
                log.error(f"Function {function_name} not found in {module_name}.")
        else:
            log.error(
                f"Function name mismatch. Expected: {self.function.get('name')}, Received: {function_name}"
            )