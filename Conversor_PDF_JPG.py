from pdf2image import convert_from_path


def convert_pdf_to_jpeg(pdf_path, output_folder):
    pages = convert_from_path(pdf_path)

    for i, page in enumerate(pages):
        image_path = f"{output_folder}/page_{i+1}.jpg"
        page.save(image_path, "JPEG")

    print("Conversão concluída.")


# Exemplo de uso:
pdf_file = "caminho/para/arquivo.pdf"
output_folder = "caminho/para/salvar/imagens"

convert_pdf_to_jpeg(pdf_file, output_folder)
