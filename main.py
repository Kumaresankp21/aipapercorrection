from ocr import generate_ocr 
from extract_question_answerkey import question_answer_content
from preprocess_ocr import preprocess_ocr_question_wise
from evalution import evaluate_exam_with_ocr_to_json
from report import generate_report

ocr_content_path = 'ilovepdf_merged.pdf'
question_paper_path = "QUESTION PAPER.pdf"
answer_key_path = "answer key.pdf"

question_paper = question_answer_content(question_paper_path)
ocr_content = generate_ocr(ocr_content_path)
answer_key = question_answer_content(answer_key_path)


# print(ocr_content)
process_ocr = preprocess_ocr_question_wise(ocr_content,question_paper)

result = evaluate_exam_with_ocr_to_json(process_ocr,answer_key)

report = generate_report(result=result)

print(report)