# ⚡ Unit Converter

### 🚀 Project 11 of 100 Python Live Projects

---

## 🌐 Live Preview

👉 [https://unit-convert.onrender.com](https://unit-convert.onrender.com)

## 💻 GitHub Repository

👉 [https://github.com/nishchup489-afk/unit_converter](https://github.com/nishchup489-afk/unit_converter)

## 🖥️ CLI Version

👉 Run `sample.py` for terminal-based interaction

---

# 🧠 Project Overview

This project is a **multi-unit conversion system** built using:

* Python (core logic)
* FastAPI (backend)
* Jinja2 (templating)
* Tailwind CSS (UI)

It allows users to convert between:

* 🌡️ Temperature
* 📏 Height
* ⚖️ Weight

The system supports both:

* CLI (for raw logic)
* Web UI (for real-world interaction)

---

# ✨ Features

* 🔥 Multi-category conversion (Temperature, Height, Weight)
* 🎯 Accurate mathematical transformations
* 🧠 Smart UI state handling (active section control)
* 💎 Glassmorphism UI with animations
* ⚡ FastAPI backend with form handling
* 🔄 Preserves user input after submission
* 🧩 Scalable structure for adding new units

---

# 📐 Mathematical Foundations

## 🌡️ Temperature Conversion

### Celsius → Fahrenheit

$$
F = \frac{9}{5}C + 32
$$

### Fahrenheit → Celsius

$$
C = \frac{5}{9}(F - 32)
$$

### Celsius → Kelvin

$$
K = C + 273.15
$$

### Kelvin → Celsius

$$
C = K - 273.15
$$

### Fahrenheit → Kelvin

$$
K = \frac{5}{9}(F - 32) + 273.15
$$

### Kelvin → Fahrenheit

$$
F = \frac{9}{5}(K - 273.15) + 32
$$

---

## 📏 Height Conversion

### Feet → Meter

$$
m = f \times 0.3048
$$

### Meter → Feet

$$
f = \frac{m}{0.3048}
$$

### Feet → Inch

$$
in = f \times 12
$$

### Inch → Feet

$$
f = \frac{in}{12}
$$

### Meter → Inch

$$
in = m \times 39.3701
$$

### Inch → Meter

$$
m = \frac{in}{39.3701}
$$

---

## ⚖️ Weight Conversion

### Kilogram → Pound

$$
lb = kg \times 2.20462
$$

### Pound → Kilogram

$$
kg = \frac{lb}{2.20462}
$$

### Kilogram → Gram

$$
g = kg \times 1000
$$

### Gram → Kilogram

$$
kg = \frac{g}{1000}
$$

### Pound → Gram

$$
g = lb \times 453.592
$$

### Gram → Pound

$$
lb = \frac{g}{453.592}
$$

---

# ⚙️ FastAPI Backend Explanation

## 📌 Core Idea

FastAPI handles form submissions and processes conversions using defined functions.

### Example Route

```python
@app.post("/temp")
def tempConvert(...):
```

### Workflow

1. Receive input via `Form(...)`
2. Identify conversion type
3. Apply correct formula
4. Return result via `TemplateResponse`

---

## 🧩 Why Jinja2?

* Inject dynamic data into HTML
* Preserve user selections
* Control UI state (active tab)

---

## 🔥 Active State System

Instead of relying on result existence:

```python
"active": "temperature"
```

Used in HTML:

```html
{% if active != 'temperature' %}hidden{% endif %}
```

👉 This ensures only one section is visible at a time.

---

# 🧪 CLI Version Logic

The CLI version focuses purely on:

* Input handling
* Mathematical computation
* Output display

No UI, just logic → perfect for understanding fundamentals.

---

# ⚠️ Mistakes We Faced (Real Lessons)

## ❌ 1. Unit mismatch

* HTML: `kilogram`
* Backend: `kg`
  👉 Caused silent failures

### ✅ Fix

Use consistent naming across frontend & backend

---

## ❌ 2. Using `disabled` in select

* Disabled values are not submitted

### ✅ Fix

Use:

```html
<option value="0">
```

---

## ❌ 3. Wrong form + Pydantic usage

* Tried to use Pydantic model with `Form()`

### ✅ Reality

* `Form()` → simple inputs
* Pydantic → JSON body

---

## ❌ 4. UI state controlled by result

```html
{% if result %}
```

👉 Breaks when multiple converters exist

### ✅ Fix

Use explicit state:

```python
"active": "height"
```

---

## ❌ 5. If-elif hell

Code becomes unscalable

### ✅ Future Improvement

Use mapping:

```python
{("kg","pound"): kg_to_pound}
```

---

# 🚀 Future Improvements

* ⚡ Real-time conversion (no page reload)
* 🧠 Universal conversion engine (no hardcoding)
* 📱 Mobile-first UI refinement
* 🌍 Add more unit systems

---

# 🏁 Conclusion

This project is more than a converter.

It teaches:

* Data flow between frontend & backend
* State management
* Clean architecture vs messy logic

👉 A small project with **real engineering depth**.

---

## 🔗 Explore More Projects

👉 [https://github.com/nishchup489-afk/100-Python-Projects](https://github.com/nishchup489-afk/100-Python-Projects)

---

🔥 Keep building. This is how you level up.
