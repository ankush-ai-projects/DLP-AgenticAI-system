from app.schemas.user import UserCreate

u = UserCreate(
    username="ankush",
    email="ankush@gmail.com",
    password="Test@1234",
    full_name="Ankush"
)
print("Schema OK:", u)
