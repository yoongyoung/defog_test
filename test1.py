from defog import Defog

defog = Defog()
# user_question = "게시판별로 콘텐츠는 몇 개인지, 게시판 이벤트 갯수는 몇 개인지 조회하는 쿼리 알려줘. 테이블 조회는 stg_board, stg_board_content 만 해줘. stg_board_content 테이블에서 course_id=6인 데이터만 조회해줘. stg_board 테이블에서 board_id=3인 데이터만 조회해줘."
# user_question = "게시판별로 콘텐츠는 몇 개인지, 게시판 이벤트 갯수는 몇 개인지 조회하는 쿼리 알려줘. 스키마는 public 스키마만 조회해줘"
# user_question = "게시판별로 콘텐츠는 몇 개인지, 게시판 이벤트 갯수는 몇 개인지 조회하는 쿼리 알려줘. 테이블은 stg_board, stg_board_event만 조회해줘"
user_question = "게시판별로 콘텐츠는 몇 개인지, 게시판 이벤트 갯수는 몇 개인지 조회하는 쿼리 알려줘. 스키마는 public, datat 스키마만 조회해줘"
answer = defog.run_query(user_question, mode="chat")
print(answer)
print("** query_generated: {answer}".format(answer=answer['query_generated']))
print("** suggestion_for_further_questions: {suggestion_for_further_questions}".format(suggestion_for_further_questions=answer['suggestion_for_further_questions']))
print("** previous_context: {previous_context}".format(previous_context=answer['previous_context']))

#print("** columns: {columns}".format(columns=answer['columns']))


#print("** data: {data}".format(data=answer['data']))`

# success question
# "How many data in stg_board table?"
# "How many data in stg_board_content table?"
# "In which category_name is the data that course_id=1 contained in the stg_course table?"
# "stg_board 테이블과 stg_board_content 테이블 조인하려면 쿼리를 어떻게 작성해야해?"
# "stg_board 테이블과 stg_board_content 테이블 조인해서, 게시글이름별로 몇 개의 콘텐츠가 작성됐는지 추출하는 쿼리 작성해줘"

# failed question
# "how many users do we have?"
# "How many total users wrote board content?"
# "게시글을 남긴 사용자는 총 몇명입니까?"
# "게시글을 작성한 총 사용자 수를 추출하려면 어떤 쿼리를 작성해야해?" (chatgpt 성공)
# "게시글 이름별로 몇 개의 콘텐츠가 작성됐는지 추출하는 쿼리 작성해줘"
# "Find which category_name the course_id=1 data included in the stg_course table belongs to in the stg_course_category table"
# "board_name별로 몇 개의 content_id가 있는지 알려면 어떻게 쿼리를 작성해야해?"


# defog = Defog(
#     api_key = "133b3eada15c6f0f2ffd221a1e1797b1717ae251497f18d1146e8e163ac36bbd",
#     db_type = "postgres",
#     # must be one of postgres, redshift, mysql, bigquery,
#     # mongo, or snowflake
#     db_creds = YOUR_DB_CREDS
#     # must be a dict in these formats, depending
#     # on your database type
#     # https://github.com/defog-ai/defog-python/blob/63af5e3ded07da356365f20bc94a194c4f7c44fa/defog/__init__.py#L110
# )

