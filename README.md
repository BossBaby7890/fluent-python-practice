# Fluent Python Practice 🚀

This repo contains my journey through **Fluent Python (2nd Edition)** by Luciano Ramalho.  
Each chapter has a set of **creative coding exercises** (not straight from the book) to help me truly internalize Python’s power.  
Mini-projects are included after groups of chapters.  

---

## 📘 Progress Roadmap

### Part I – Data Structures

#### Chapter 1: The Python Data Model ✅
- **Exercise 1: Vector2D**
  Implement a lightweight 2D vector class with operator overloading for `+`, `-`, scalar multiplication, and equality.  
  - `Vector2D(2,3) + Vector2D(1,1) → Vector2D(3,4)`  
  - Must support `len(v)` and `abs(v)` (magnitude).  
  - Ensure it is hashable.  

- **Exercise 2: PixelGrid**
  Design a `PixelGrid` class that models a 2D grid of pixels.  
  - Each pixel is `(r,g,b)` where values are 0–255.  
  - Support `grid[row, col]` indexing for pixel access.  
  - Support slicing (e.g., `grid[0:10, 0:10]` → sub-grid).  
  - Implement `__iter__` so you can do `for pixel in grid:`.  

- **Exercise 3: Polynomial**
  Create a `Polynomial` class for math expressions like `3x² + 2x + 1`.  
  - Store coefficients in a dict `{power: coefficient}`.  
  - Support addition (`p1 + p2`), evaluation (`p(x)`), and string display (`"3x² + 2x + 1"`).  
  - Equality (`==`) should compare polynomials.  

---

#### Upcoming:
- Chapter 2: Sequences → fun with custom slicing + data compression.  
- Chapter 3: Dictionaries & Sets → word frequency + inverted index builder.  
- Chapter 4: Unicode vs Bytes → text normalization challenges.  
- Mini-Project (after Part I): **Text Analyzer Tool** that ingests a document and gives insights (word counts, Unicode handling, etc.).  

---

## 💡 Guidelines
- Exercises live in `exercises/`.  
- My personal solutions go in `solutions/`.  
- Mini-projects go in their own folder under each part.  

---

## 🔥 Goal
Finish all chapters with working code and mini-projects within **X weeks** while building a **portfolio of Python practice**.  
