Simon's game
---
### Par Camille INGOUF et Benoît Verhaghe

---

Fonctionnement
---

Le jeu se lance avec un cercle blanc. Il suffit d'appuyer sur le bouton "a" ou "b" pour lancer une partie.

Un pattern de 8 étapes est défini aléatoirement.
La première étape du pattern est montrée, puis il suffit de la copier en touchant les pads correspondants.

Lors de la victoire, une animation est jouée puis une cercle vert est affiché.
Lors de la défaite, un cercle rouge est affiché.

Pour relancer une partie, il suffit d'appuyer brièvement sur reset.

---

Bilan
---

Les problèmes rencontrés étaient assez simple à surmonter. Se re-familiariser avec le python, comprendre la documentation et savoir l'appliquer, puis réflechir à la conception du jeu.

On a choisi ce petit jeu pour pouvoir mettre en pratique la maîtrise du son et de la lumière. L'algo n'est pas si basique alors il nous a permis de lier la maîtrise de l'outil et la mise en place d'un jeu.

D'autres problèmes se sont imposés lorsqu'il a fallut choisir comment communiquer au joueur ce qu'il devait faire et l'état de la partie. Aussi comment récupérer les réponses du joueur, sans que ce soit trop embêtant pour lui de jouer.

On a choisi de faire des groupes de 3 pixels donc seulement 4 "boutons" avec lesquels le joueur peut intéragir. Il appuiera naturalement à côté des pixels sur les pads sans se soucier de la précision de son "toucher"  