from main import dp, client
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.enums.chat_action import ChatAction
from aiogram.types import Message
from app.opengpt import answer
from fsm.states import WaitState

router = Router()


@router.message(WaitState.msgPrinted)
async def wait_print_answer(message: Message):
    await message.answer("Иоша печатает ответ...")


@router.message(F.text)
async def print_answer(message: Message, state: FSMContext):
    await state.set_state(WaitState.msgPrinted)
    await client.send_chat_action(message.chat.id, ChatAction.TYPING)
    resp = await answer(message.text)
    await message.answer(resp)
    await state.clear()
