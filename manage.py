import argparse
import asyncio

from backend import User, db_manager


async def create_user():
    name = input('Enter name for new user (profile): ')
    email = input('Enter email for new user (profile): ')
    password = input('Enter password for new user (profile): ')
    
    while input('Re-Enter password: ') != password:
        print('Incorrect. Try again')

    print(f'name: {name}\nemail: {email}\npassword: {password}\n\n')

    async with db_manager.session() as session:
        users = await User.all(session=session)

        for u in users:
            u.active = False

        user = await User.create(session=session, name=name, email=email, password=password, active=True)

    print('User created!')
    return None

async def switch_user():
    name = input('Enter username of profile you want to enter: ')

    async with db_manager.session() as session:
        users = await User.all(session=session)

        for u in users:
            u.active = False

        user = await User.get(session=session, field=User.name, value=name)
        user.active = True

        await session.commit()

        print(f'Switched to: {name}')


def main():
    parser = argparse.ArgumentParser(description="profile controlls")
    subparsers = parser.add_subparsers(dest="command")

    # Додаємо команди
    subparsers.add_parser("createuser", help="create new profile (user)")
    subparsers.add_parser("switch", help="switch between local profiles")

    args = parser.parse_args()

    if args.command == "createuser":
        asyncio.run(create_user())
    elif args.command == "switch":
        asyncio.run(switch_user())
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
