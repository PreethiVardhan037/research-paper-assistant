def chunk_text(text, chunk_size=1000):
    paragraphs = text.split("\n")

    chunks = []
    current = ""

    for para in paragraphs:
        if len(current) + len(para) < chunk_size:
            current += para + "\n"
        else:
            chunks.append(current)
            current = para + "\n"

    if current:
        chunks.append(current)

    return chunks