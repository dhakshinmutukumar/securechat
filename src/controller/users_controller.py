from db.users_repo import usersrepo

_repo = usersrepo()


class CreateUser:
    def __call__(self, username: str, password: str, email: str) -> None:
        _repo.add(username, password, email)


class ListUsers:
    def __call__(self) -> list[str]:
        return _repo.getall()


class UserExists:
    def __call__(self, username: str) -> bool:
        return _repo.user_exists(username)


class ValidateUser:
    def __call__(self, username: str, password: str) -> bool:
        return _repo.validate_user(username, password)


class EmailExists:
    def __call__(self, email: str) -> bool:
        return _repo.email_exists(email)
