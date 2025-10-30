def predict_image(file_path: str) -> str:
    """
    Test uchun minimal funksiya.
    Fayl nomida 'sick' bo‘lsa kasallik, aks holda sog‘lom.
    """
    if "sick" in file_path.lower():
        return "Kasallik aniqlangan"
    else:
        return "O‘simlik sog‘lom"
