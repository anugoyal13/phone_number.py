from typing import List, Dict, Union


class PhoneNumberAssessment:
    def list_words_matching_phone_number(self, phone_number: str, input_words: List[str]):
        a = []
        number = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["gp", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        new_val = ""
        p = ""
        for x in input_words:

            for i in x:
                if i.lower() in number["2"]:
                    ref = "2"
                elif i.lower() in number["3"]:
                    ref = "3"
                elif i.lower() in number["4"]:
                    ref = "4"
                elif i.lower() in number["5"]:
                    ref = "5"
                elif i.lower() in number["6"]:
                    ref = "6"
                elif i.lower() in number["7"]:
                    ref = "7"
                elif i.lower() in number["8"]:
                    ref = "8"
                elif i.lower() in number["9"]:
                    ref = "9"
                else:
                    ref = ""

                if ref in new_val:
                    ref = ""
                else:
                    ref = ref
                new_val = new_val + ref
                new_val = "".join(sorted(new_val))
            if new_val != p:
                if new_val in phone_number:
                    a.append(x)
                    p = new_val
        return a


class TestPhoneNumberAssessment:
    def __init__(self):
        self.phone_number_assessment = PhoneNumberAssessment()

    @staticmethod
    def get_tests() -> List[Dict[str, Union[str, List[str]]]]:
        tests = [
            {
                "phone_number": "36",
                "input_words": ["foo"],
                "expected_output_words": ["foo"],
            },
            {
                "phone_number": "2367",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "012367",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "!a2367Z?",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": ["foo", "bar"],
            },
            {
                "phone_number": "2367",
                "input_words": ["foo", "f00", "bAr", "ba$r"],
                "expected_output_words": ["foo", "bAr"],
            },
            {
                "phone_number": "4589",
                "input_words": ["foo", "bar", "baz"],
                "expected_output_words": [],
            },
            {"phone_number": "4589", "input_words": [], "expected_output_words": []},
        ]

        return tests

    def run_individual_test(
        self, index: int, test: Dict[str, Union[str, List[str]]]
    ) -> bool:
        resulting_output_words = (
            self.phone_number_assessment.list_words_matching_phone_number(
                test["phone_number"], test["input_words"]
            )
        )
        test_passed = resulting_output_words == test["expected_output_words"]

        if not test_passed:
            print(f"Test {str(index + 1)} failed!")
            print(f"Phone number: {test['phone_number']}")
            print(f"Input words: {test['input_words']}")
            print(f"Resulting output words: {resulting_output_words}")
            print(f"Expected output words: {test['expected_output_words']}\n")

        return test_passed

    def test_phone_number_assessment_solution(self):
        tests = self.get_tests()
        all_tests_passed = all(
            self.run_individual_test(index, test) for index, test in enumerate(tests)
        )
        if all_tests_passed:
            print("Congrats, all tests passed!")


if __name__ == "__main__":
    TestPhoneNumberAssessment().test_phone_number_assessment_solution()

