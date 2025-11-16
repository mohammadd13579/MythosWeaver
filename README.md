MythosWeaver
============

**MythosWeaver** is a creative Python project that procedurally generates a unique, internally-consistent micro-mythology. It builds a pantheon of gods from the ground up, complete with names, domains (e.g., 'War', 'Sea', 'Wisdom'), personalities, and a family tree. It then generates a short creation myth based on the gods it just invented.

Features
--------

-   **Generative Names:** Creates unique names for gods from syllabic parts.

-   **Logical Domains:** Assigns gods unique domains of power.

-   **Family Tree:** Generates a consistent family tree with 2 "Primordial" gods, a second generation of children, and a third generation of grandchildren.

-   **Relational Logic:** Automatically links parents, children, spouses, and siblings.

-   **Procedural Myth:** Generates a "Mad-Libs" style creation myth using the names and domains of the primordial gods.

-   **OOP Design:** Clean, extensible, and easy-to-read code using `God` and `Pantheon` classes.

How to Run
----------

This project uses only Python's standard `random` library, so no external packages are required.

1.  Ensure you have Python 3.6 or newer installed.

2.  Place the `mythos_weaver` folder and the `main.py` file in the same directory.

3.  Run the main script from your terminal:

    ```
    python main.py
    ```

4.  Each time you run the script, a new mythology will be generated and printed to the console.

**Example Output:**

```
--- Weaving the myth of the the Whispering Stars ---
Generating 9 deities...
Pantheon populated.

--- The Creation Myth ---
All was Chaos until Thosi dreamed the Sky from nothing. Thosi grew lonely
and shaped Alothea from pure raw Magic. As opposites, their balance created
all that is. Their descendants, Helora, Arra, and Elos, were given dominion
over the world, but battled for supremacy in their power.

--- The Pantheon of the Whispering Stars ---

**Generation 0 (The Primordials)**
**Thosi**, The Trickster God of Sky.
    - Sibling to: Alothea.
    - Spouse to Alothea.
    - Parent to: Helora, Arra, Elos.

**Alothea**, The Benevolent God of Magic.
    - Sibling to: Thosi.
    - Spouse to Thosi.
    - Parent to: Helora, Arra, Elos.

**Generation 1 (The Gods)**
**Helora**, The Reclusive God of Sea.
    - Child of Thosi and Alothea.
    - Sibling to: Arra, Elos.
    - Spouse to Arra.
    - Parent to: Zera, Pos.

**Arra**, The Wrathful God of War.
    - Child of Thosi and Alothea.
    - Sibling to: Helora, Elos.
    - Spouse to Helora.
    - Parent to: Zera, Pos.

**Elos**, The Wise God of Wisdom.
    - Child of Thosi and Alothea.
    - Sibling to: Helora, Arra.
    - Parent to: Raos, Alona.

**Generation 2 (The Gods)**
**Zera**, The Jealous God of Earth.
    - Child of Helora and Arra.

**Pos**, The Artistic God of Sun.
    - Child of Helora and Arra.

**Raos**, The Chaotic God of Fire.
    - Child of Elos.

**Alona**, The Nurturing God of Hearth.
    - Child of Elos.
```

How to Extend
-------------

This project is designed to be a foundation. Here are some ideas for extending it:

-   **Generate Heroes & Monsters:** Create new classes for `Hero` and `Monster`. A `Hero` could have a divine parent from the pantheon.

-   **Generate Artifacts:** Create a `generate_artifact()` method for the `Pantheon` class that creates a legendary item (e.g., "The Spear of {God.Name}" or "The {Domain} Crown").

-   **More Complex Myths:** Expand the `MYTH_TEMPLATES` or create a new method (`generate_war_myth()`) that picks gods with 'War' or 'Wrathful' personalities to battle each other.

-   **Assign Attributes:** Give gods weighted attributes (e.g., `strength: 1-10`, `magic: 1-10`) based on their domain.

-   **Web Interface:** Use Flask or Django to turn this into a simple web app where users can click a button to generate and view a new mythology.
