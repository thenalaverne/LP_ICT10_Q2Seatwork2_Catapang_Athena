from pyscript import document, display

def calculate_gwa(event):
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    try:
        sci = float(document.getElementById("science").value)
        math = float(document.getElementById("math").value)
        eng = float(document.getElementById("english").value)
        fil = float(document.getElementById("filipino").value)
        ict = float(document.getElementById("ict").value)
        pe = float(document.getElementById("pe").value)

        gwa = (sci + math + eng + fil + ict + pe)/6
        result = (
            f"Name: {fname} {lname}\n\n"
            f"Science: {sci}\n"
            f"Math: {math}\n"
            f"English: {eng}\n"
            f"Filipino: {fil}\n"
            f"ICT: {ict}\n"
            f"PE: {pe}\n\n"
            f"Your General Weighted Average is: {gwa:.2f}"
        )
        display(result, target="output")


except ValueError:
        display("Please fill in all fields", target="output")