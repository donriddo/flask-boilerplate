from setup import db
from src.users.user_model import User


def create_user(data):
    user = User(first_name=data['first_name'],
                last_name=data['last_name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return user.to_json()


def fetch_user(id):
    user = User.query.get(id)
    if user:
        return user.to_json()
    else:
        return None


def fetch_all_users(query, page=1, per_page=5):
    result = User.query
    for key in query:
        if query[key] is None:
            continue

        if key == 'email':
            result = result.filter_by(email=query["email"])
        elif key == 'first_name':
            result = result.filter_by(first_name=query["first_name"])
        elif key == 'last_name':
            result = result.filter_by(last_name=query["last_name"])

    result = result.order_by(User.id.desc()).paginate(
        page,
        per_page,
        error_out=False
    )

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


def update_user(id, data):
    user = User.query.get(id)
    if not user:
        return None

    for key in data:
        if hasattr(user, key):
            setattr(user, key, data[key])

    db.session.commit()
    return user.to_json()


def delete_user(id):
    user = User.query.get(id)
    if not user:
        return None

    db.session.delete(user)
    db.session.commit()
    return user.to_json()
