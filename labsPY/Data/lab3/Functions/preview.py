def preview_art(art):
    print("Preview of your ASCII Art:")
    print(art)
    approval = input("Are you satisfied with the preview? (yes/no): ").strip().lower()
    return approval == "yes"
