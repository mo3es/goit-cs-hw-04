from faker import Faker
import os
from random import randint

fake = Faker("en_US")
PARAGRAPHS_UPPER_BOUND = 10000
FILES_UPPER_BOUND = 30
LOWER_BOUND = 1
REQUEST_TYPE_PARAGRAPHES = "paragraphes"
REQUEST_TYPE_FILES = "files"

"""
Встановлюємо шлях до директорії src/texts, до якої мають бути збережені згенеровані тексти. Дана директорія має знаходитись у директорії srcб яка, своєю чергою, розташована у корені проекту. Відповіно, нам необхідно знайти
шлях до попередньої директорії - тобто, від абсолютного шляху до файла-генератора (os.path.abspath(__file__)) знайти 
директорію - os.path.dirname(os.path.abspath(__file__)), від якої, відповідно, знайти батьківську директорію - os.path.dirname(os.path.dirname(os.path.abspath(__file__)). До отриманого шляху додати цільову директорію - os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src/texts').
"""
path_to_save = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src/texts"
)


def generate_text(length=0) -> str:
    quantity = length if length > 0 else randint(LOWER_BOUND, PARAGRAPHS_UPPER_BOUND)
    content = "\n\n".join(fake.paragraphs(nb=quantity))
    return content


def get_quantity(request_type_string: str) -> int:
    upper_bound = (
        PARAGRAPHS_UPPER_BOUND
        if request_type_string == REQUEST_TYPE_PARAGRAPHES
        else FILES_UPPER_BOUND
    )

    while True:
        quantity = input(
            f"How many {request_type_string} you want to generate? (from {LOWER_BOUND} to {upper_bound}) "
        )
        
        if quantity.isnumeric():
            quantity = int(quantity)
            if quantity not in range(LOWER_BOUND, upper_bound):
                quantity = 0
                print(
                    "Inputed quantity is not in correct bounds, the random quantity will be set."
                )
            return quantity
        else:
            print(f"Input is not numeric - {quantity}")


def generate():
    files_quantity = get_quantity(REQUEST_TYPE_FILES)
    files_quantity = (
        files_quantity
        if files_quantity != 0
        else randint(LOWER_BOUND, FILES_UPPER_BOUND)
    )
    if not os.path.exists(path_to_save):
        try:
            os.makedirs(path_to_save)
        except OSError as e:
            print(
                f"An ERROR occures: destination directory {path_to_save} can`t be created: {e}"
            )
            exit()

    for i in range(files_quantity):
        paragraphs_quantity = get_quantity(REQUEST_TYPE_PARAGRAPHES)
        file_path = os.path.join(path_to_save, f"generated_text_{i + 1}.txt")
        content = generate_text(paragraphs_quantity)

        try:
            with open(file_path, "w", encoding="UTF-8") as f:
                f.write(content)
            print(
                f"{i + 1}-th fake text was generated succesfully and saved at {file_path}"
            )
        except IOError as e:
            print(f"An ERROR occured during {file_path} saving: {e}.")
    print("Generation done")


if __name__ == "__main__":
    generate()
