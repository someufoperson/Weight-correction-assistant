from aiogram.fsm.context import FSMContext

async def get_language(state: FSMContext) -> str:
    data = await state.get_data()
    try:
        language = data["language"]
    except Exception as e:
        print(e)
    
    return language