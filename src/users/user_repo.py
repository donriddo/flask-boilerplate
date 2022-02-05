from setup import db
from src.users.user_model import User


def create_user(record):
    user = User(first_name=record['first_name'],
                last_name=record['last_name'], email=record['email'])
    db.session.add(user)
    db.session.commit()
    return user.to_json()


def fetch_user(name=None, email=None):
    user = User.objects(name=name, email=email).first()
    if user:
        return user.to_json()
    else:
        return None


def fetch_all_users(page=1, per_page=5):
    result = User.query.order_by(User.id.desc()).paginate(
        page, per_page, error_out=False)

    return {
        "meta": {
            "current_page": result.page,
            "total_pages": result.pages,
            "total": result.total,
            "has_prev": result.has_prev,
            "next_page": result.next_num,
            "has_next": result.has_next,
        },
        "data": list(map(lambda user: user.to_json(), result.items))
    }
