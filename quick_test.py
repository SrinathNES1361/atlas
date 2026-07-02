from atlas.adapters.pymupdf import RawDocument

with RawDocument("examples/yjoh-23-187.pdf") as pdf:
    print(pdf.page_count)

    for page in pdf.pages():
        print(page.number)

        print(page.width)

        print(page.height)

        print(page.data.keys())
