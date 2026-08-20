from openai import OpenAI
from src.logger import log_event

def generate_rag_response(query, retrieved_contexts):
    """
    توليد إجابة ذكية ودقيقة باستخدام OpenRouter API بناءً على السياق المسترجع وسؤال المستخدم
    """
    if not retrieved_contexts:
        log_event("WARNING", "No context provided for LLM generation.")
        return "I am sorry, but I couldn't find relevant information in the university knowledge base to answer your question."

    # دمج النصوص المسترجعة لتكون سياقاً (Context) للنموذج
    context_text = "\n".join(retrieved_contexts)

    try:
        # ربط OpenRouter باستخدام مفتاحك
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key="",
        )

        completion = client.chat.completions.create(
            model="openai/gpt-4o-mini", # موديل سريع واقتصادي ممتاز جداً للمشاريع
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful university assistant. Answer the user's question accurately and concisely based ONLY on the provided context."
                },
                {
                    "role": "user",
                    "content": f"Context:\n{context_text}\n\nQuestion:\n{query}"
                }
            ]
        )

        response = completion.choices[0].message.content
        log_event("SUCCESS", "Successfully generated RAG response using OpenRouter.")
        return response

    except Exception as e:
        log_event("ERROR", f"Failed to generate response from OpenRouter: {str(e)}")
        # كود احتياطي في حال حدثت أي مشكلة بالاتصال
        return f"**Question:** {query}\n\n**Answer:** Based on the university records, {context_text}"