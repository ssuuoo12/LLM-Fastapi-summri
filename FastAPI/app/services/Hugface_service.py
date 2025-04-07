from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class HuggingFaceSummaryService:
    def __init__(self, model_name="lcw99/t5-base-korean-text-summary"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name) # 토크나이저와 모델을 불러오기
        self.prefix = "summarize: "
        self.max_input_length = 512
        self.max_output_length = 100
        # 입력 문장은 512 토큰까지 자르고,
        # 출력은 최대 100토큰까지 생성하게 제한

    def generate_summary(self, text: str):
        prompt = self.prefix + text
        inputs = self.tokenizer(prompt, return_tensors="pt", truncation=True, max_length=self.max_input_length)
        # return_tensors="pt" → PyTorch 텐서로 반환
        # truncation=True → 길면 자르고
        outputs = self.model.generate(**inputs, num_beams=4, do_sample=True, min_length=10, max_length=self.max_output_length)
        # **inputs : 토크나이저로부터 얻은 입력 텐서 (input_ids 등)
        # num_beams=4 → Beam search 사용 (더 나은 결과 생성)
        # do_sample=True → 약간의 랜덤성 부여 (다양한 문장 가능)
        # min_length=10 → 최소 생성 길이 제한
        summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # generate()는 여러 문장을 생성할 수 있기 때문에 결과가 리스트로 나와요.
        # [0]은 그 중 첫 번째 결과를 출력
        return summary
