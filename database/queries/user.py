from database.database import async_session
from database.models.user import UserOrm
from sqlalchemy import select, update
from sqlalchemy.sql import func

from log_config import logger

class UserQueries:

    @staticmethod
    async def is_exitsts(user_id: int) -> bool:
        """Checks user_id for presence in the db"""
        async with async_session() as session:
            query = (
                select(UserOrm)
                .where(UserOrm.user_id == user_id)
            )

            res = await session.execute(query)
            return False if not res.scalar() else True

    @staticmethod
    async def new_user_id(user_id: int):
        """Creates a record in the database using only user_id"""
        exists = await UserQueries.is_exitsts(user_id=user_id)

        if not exists:
            async with async_session() as session:
                new_user = UserOrm(user_id=user_id)
                try:
                    session.add(new_user)
                    await session.commit()
                    logger.info(msg="The user adding to database")
                except Exception as e:
                    logger.error(msg=e)
        elif exists:
            logger.error(msg="The user exists in the database")

    @staticmethod
    async def edit_lang(user_id: int, language: str):
        """Edit language user"""
        async with async_session() as session:
            query = (
                update(UserOrm)
                .where(UserOrm.user_id == user_id)
                .values({"lang": language})
            )
            await session.execute(query)
            await session.commit()
        
    @staticmethod
    async def edit_name(user_id: int, name: str):
        """Edit name user"""
        async with async_session() as session:
            query = (
                update(UserOrm)
                .where(UserOrm.user_id == user_id)
                .values({"name": name})
            )
            await session.execute(query)
            await session.commit()

    @staticmethod
    async def edit_age(user_id: int, age: int):
        """Edit age user"""
        async with async_session() as session:
            query = (
                update(UserOrm)
                .where(UserOrm.user_id == user_id)
                .values({"age": age})
            )
            await session.execute(query)
            await session.commit()

    # @staticmethod
    # async def new_user(user_id: int, 
    #                    age: int, 
    #                    actual_weight: float,
    #                    height: int,
    #                    desired_weight: float,
    #                    gender: str,
    #                    undesirable_products: str,
    #                    preferred_products: str,
    #                    language: str):
    #     """Create new user with existence check"""
    #     exists = await UserQueries.is_exitsts(user_id=user_id)

    #     if not exists:
    
    #         async with async_session() as session:
    #             new_user = UserOrm(user_id=user_id,
    #                                age=age,
    #                                actual_weight=actual_weight,
    #                                height=height,
    #                                desired_weight=desired_weight,
    #                                gender=gender,
    #                                undesirable_products=undesirable_products,
    #                                preferred_products=preferred_products,
    #                                language=language)
    #             try:
    #                 session.add(new_user)
    #                 await session.commit()
    #             except Exception as e:
    #                 logger.error(msg=e)

    #     elif exists:
    #         logger.error(msg="The user exists in the database")

    @staticmethod
    async def update_actual_weight(user_id: int, actual_weight: float):
        async with async_session() as session:
            query = (

            )