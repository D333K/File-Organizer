import os

images_extension = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".svg", ".ico", ".heic"}
videos_extension = {".mp4", ".mkv", ".webm", ".avi", ".mov", ".mpeg", ".mpg", ".flv", ".3gp"}
audio_extension = {".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".opus", ".wma"}
documents_extension = {".txt", ".md", ".rtf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf"}
code_extension = {".py", ".pyw", ".js", ".ts", ".html", ".htm", ".css", ".cpp", ".c", ".h", ".hpp", ".java", ".cs", ".php", ".go", ".rs", ".sh", ".bat", ".ps1", ".json"}
archives_extension = {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".deb"}
disk_img_extension = {".iso", ".img", ".dmg"}

def where_put_it(file_name) -> str:
    """This Method Will Return String Of The Appropriate Type Of Folders."""

    extension = os.path.splitext(file_name)[1]

    if extension.lower() in images_extension:
        return "Images"
    
    if extension.lower() in videos_extension:
        return "Videos"

    if extension.lower() in audio_extension:
        return "Audio"
    
    if extension.lower() in documents_extension:
        return "Documents"

    if extension.lower() in code_extension:
        return "Code"

    if extension.lower() in archives_extension:
        return "Archives"

    if extension.lower() in disk_img_extension:
        return "Disk Images"

    return "Others"

