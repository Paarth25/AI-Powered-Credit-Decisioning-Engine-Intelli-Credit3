from jinja2 import Template

class CAMGenerator:

    def generate(self, data):

        template_text = """
        CREDIT APPRAISAL MEMO

        Character:
        {{character}}

        Capacity:
        {{capacity}}

        Capital:
        {{capital}}

        Collateral:
        {{collateral}}

        Conditions:
        {{conditions}}

        Final Recommendation:
        {{recommendation}}
        """

        template = Template(template_text)
        return template.render(**data)