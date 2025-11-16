"""
MythosWeaver: A Procedural Mythology Generator
This module contains the core classes for generating a pantheon of gods,
their relationships, and a basic creation myth.
"""

import random

# --- Data Pools for Generation ---

DOMAINS = [
    'Sky', 'Sea', 'Earth', 'Underworld', 'Sun', 'Moon', 'War', 'Wisdom',
    'Fire', 'Hearth', 'Craft', 'Magic', 'Darkness', 'Light', 'Nature',
    'Time', 'Fate', 'Music', 'Art', 'Love', 'Death', 'Birth'
]

PERSONALITIES = [
    'Benevolent', 'Malevolent', 'Chaotic', 'Lawful', 'Trickster',
    'Nurturing', 'Wrathful', 'Wise', 'Artistic', 'Reclusive', 'Jealous'
]

# Simple name generation syllables
NAME_STARTS = ['A', 'El', 'Tho', 'Ra', 'Ze', 'He', 'Po', 'Ar', 'Lo']
NAME_MIDS = ['la', 'ro', 'mi', 'ra', 'o', 'llo', 'the', 'si']
NAME_ENDS = ['ius', 'os', 'on', 'es', 'a', 'ia', 'us', 'na', 'or']

# --- Myth Templates ---

MYTH_TEMPLATES = [
    (
        "In the timeless beginning, there was only the {void}. From it emerged {primordial1}, the "
        "First, and {primordial2}, the All-Heart. They {verb} the world from {element}, shaping the "
        "first dawn. Their children, {child_list}, {action} upon the new world, and thus the age of gods began."
    ),
    (
        "Before time, {primordial1} slept in the {void}. A dream of {element} gave birth to {primordial2}. "
        "Together, they danced, and their dance {verb} the stars and the {domain} itself. "
        "From their union came {child_list}, the first pantheon, who {action} the mortals."
    ),
    (
        "All was {void} until {primordial1} {verb} the {domain} from nothing. {primordial1} grew lonely "
        "and shaped {primordial2} from pure {element}. As opposites, their balance created all that is. "
        "Their descendants, {child_list}, were given dominion over the world, but {action} in their power."
    )
]


class God:
    """
    Represents a single god in the pantheon.
    Each god has a name, domain, personality, and relationships.
    """
    def __init__(self, name, domain, personality):
        self.name = name
        self.domain = domain
        self.personality = personality
        self.generation = 0  # 0 for primordials, 1 for their children, etc.
        self.parents = []
        self.spouse = None
        self.children = []
        self.siblings = []

    def __repr__(self):
        """String representation for debugging."""
        return f"<God: {self.name} (Gen {self.generation})>"

    def describe(self):
        """Returns a formatted string describing the god."""
        description = f"**{self.name}**, The {self.personality} God of {self.domain}.\n"
        
        # Describe relationships
        if self.parents:
            parent_names = " and ".join([p.name for p in self.parents])
            description += f"    - Child of {parent_names}.\n"
        
        if self.siblings:
            sibling_names = ", ".join([s.name for s in self.siblings if s != self])
            if sibling_names:
                description += f"    - Sibling to: {sibling_names}.\n"

        if self.spouse:
            description += f"    - Spouse to {self.spouse.name}.\n"

        if self.children:
            child_names = ", ".join([c.name for c in self.children])
            description += f"    - Parent to: {child_names}.\n"
            
        return description


class Pantheon:
    """
    Represents the entire collection of gods and the associated creation myth.
    Manages the generation and relationships of all gods.
    """
    def __init__(self, pantheon_name):
        self.pantheon_name = pantheon_name
        self.gods = []
        self.domains_in_use = set()
        print(f"--- Weaving the myth of the {self.pantheon_name} ---")

    def _generate_name(self):
        """Generates a simple, unique name for a god."""
        while True:
            name = (
                random.choice(NAME_STARTS) +
                random.choice(NAME_MIDS) +
                random.choice(NAME_ENDS)
            )
            if name not in [g.name for g in self.gods]:
                return name

    def _get_unique_domain(self):
        """Selects a domain not already in use."""
        available_domains = [d for d in DOMAINS if d not in self.domains_in_use]
        if not available_domains:
            # Fallback if we run out of unique domains
            return random.choice(DOMAINS)
        
        domain = random.choice(available_domains)
        self.domains_in_use.add(domain)
        return domain

    def _create_god(self, generation, parents=None):
        """Helper method to create a new god and add them to the pantheon."""
        name = self._generate_name()
        domain = self._get_unique_domain()
        personality = random.choice(PERSONALITIES)
        
        new_god = God(name, domain, personality)
        new_god.generation = generation
        
        if parents:
            new_god.parents = parents
            for parent in parents:
                parent.children.append(new_god)
        
        self.gods.append(new_god)
        return new_god

    def populate(self, num_gods=8):
        """
        Populates the pantheon with a specified number of gods,
        creating logical generations.
        """
        if num_gods < 2:
            print("A pantheon needs at least two primordial gods.")
            return

        print(f"Generating {num_gods} deities...")

        # 1. Create two primordial gods (Gen 0)
        primordial1 = self._create_god(generation=0)
        primordial2 = self._create_god(generation=0)
        
        # Link primordials as spouses and siblings
        primordial1.spouse = primordial2
        primordial2.spouse = primordial1
        primordial1.siblings.append(primordial2)
        primordial2.siblings.append(primordial1)
        
        gen1_parents = [primordial1, primordial2]
        gods_to_create = num_gods - 2
        
        if gods_to_create <= 0:
            return # We only have the two primordials

        # 2. Create the second generation (Gen 1) - children of primordials
        # Aim for 2-4 children in Gen 1
        num_gen1 = min(random.randint(2, 4), gods_to_create)
        gen1_gods = []
        for _ in range(num_gen1):
            god = self._create_god(generation=1, parents=gen1_parents)
            gen1_gods.append(god)
            
        # Link Gen 1 as siblings
        for god in gen1_gods:
            god.siblings = [g for g in gen1_gods if g != god]
            
        gods_to_create -= num_gen1
        if gods_to_create <= 0:
            return

        # 3. Create the third generation (Gen 2) - children of Gen 1
        # Randomly assign parents from Gen 1
        possible_gen2_parents = gen1_gods[:]
        
        for _ in range(gods_to_create):
            # Try to find a pair of parents
            if len(possible_gen2_parents) >= 2:
                parent1 = random.choice(possible_gen2_parents)
                parent2 = random.choice([g for g in gen1_gods if g != parent1])
                
                # Assign them as spouses if not already
                if not parent1.spouse and not parent2.spouse:
                    parent1.spouse = parent2
                    parent2.spouse = parent1
                
                parents = [parent1, parent2]
                
            # Fallback to a single parent if needed
            elif possible_gen2_parents:
                parents = [random.choice(possible_gen2_parents)]
            else:
                # Should not happen, but fallback to primordials
                parents = gen1_parents
                
            self._create_god(generation=2, parents=parents)

        print("Pantheon populated.")

    def generate_creation_myth(self):
        """
        Generates a simple, template-based creation myth using the
        generated primordial gods.
        """
        print("\n--- The Creation Myth ---")
        
        # Find our primordial gods (Gen 0)
        primordials = [g for g in self.gods if g.generation == 0]
        if len(primordials) < 2:
            return "In the beginning... there was an error. The primordials are missing."
            
        p1 = primordials[0]
        p2 = primordials[1]
        
        # Find their children (Gen 1)
        children = [g for g in self.gods if g.generation == 1]
        child_list = "no one"
        if children:
            child_list = ", ".join([c.name for c in children])
            
        # Pick a template and fill it
        template = random.choice(MYTH_TEMPLATES)
        myth = template.format(
            void=random.choice(['Void', 'Chaos', 'Silence', 'Endless Dark']),
            primordial1=p1.name,
            primordial2=p2.name,
            verb=random.choice(['sung', 'forged', 'dreamed', 'tore', 'birthed']),
            element=random.choice(['primordial Fire', 'the deep Sea', 'raw Magic', 'pure Light']),
            domain=p1.domain,
            child_list=child_list,
            action=random.choice([
                'brought order', 'battled for supremacy', 'guided', 'grew jealous'
            ])
        )
        return myth

    def display_pantheon(self):
        """Prints the details of the entire pantheon."""
        print(f"\n--- The Pantheon of {self.pantheon_name} ---")
        
        # Sort gods by generation for a logical display
        sorted_gods = sorted(self.gods, key=lambda g: g.generation)
        
        current_gen = -1
        for god in sorted_gods:
            if god.generation != current_gen:
                current_gen = god.generation
                print(f"\n**Generation {current_gen} (The {'Primordials' if current_gen == 0 else 'Gods'})**")
            
            print(god.describe())
