import praw

def get_user_data(username):
    reddit = praw.Reddit(
        client_id="-7h1TZ-o4yNEh7B13oJnag",
        client_secret="T3aOGAcsrG_4FrKYKT0qU_EHPLvISA",
        user_agent="reddit-persona-generator-script",
        check_for_async=False
    )
    reddit.read_only = True  # ✅ Enable public access without login

    user = reddit.redditor(username)
    posts, comments = [], []

    for submission in user.submissions.new(limit=5):  # 🔽 Reduced to avoid LLM overload
        post_info = (
            f"[POST] {submission.title}\n"
            f"{submission.selftext}\n"
            f"[Source] https://www.reddit.com{submission.permalink}\n"
        )
        posts.append(post_info)

    for comment in user.comments.new(limit=5):  # 🔽 Reduced to avoid 400 errors
        comment_info = (
            f"[COMMENT] {comment.body}\n"
            f"[Source] https://www.reddit.com{comment.permalink}\n"
        )
        comments.append(comment_info)

    return posts, comments
