
# from app.prompts.rewrite import (
#     REWRITE_PROMPT,
# )


# class QueryRewriter:

#     def __init__(
#         self,
#         llm,
#     ):
#         self.llm = llm

#     def rewrite(
#         self,
#         query: str,
#     ) -> str:

#         prompt = REWRITE_PROMPT.format(
#             query=query,
#         )

#         response = (
#             self.llm.generate(
#                 prompt=prompt,
#                 provider="groq",
#             )
#         )

#         return response.strip()
        