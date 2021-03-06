Στοιχεία Σώματος (Body Elements)
************************************

Με τον όρο *στοιχεία σώματος* εννοούμε όλες εκείνες τις "δομές" ή *κατασκευές* που μπορούμε να ενσωματώσουμε σαν περιεχόμενο, σε ένα κείμενο. Οι απλές παράγραφοι κειμένου, οι πίνακες, οι εικόνες κ.λπ., είναι τέτοιες δομές. Για κάθε μία τέτοια δομή, η reST παρέχει τα κατάλληλα συντακτικά εργαλεία για να τις χρησιμοποιήσουμε.

Στη συνέχεια παραθέτουμε τα βασικά στοιχεία σώματος που μπορούμε να χρησιμοποιήσουμε στη reST. Λεπτομέρειες και παραδείγματα, δίνονται σε αντίστοιχες ενότητες.


.. _rest-concept-paragraph-ref:

Παράγραφοι (Paragraphs)
==========================

Η παράγραφος είναι το βασικό μπλοκ κειμένου σε ένα κείμενο γραμμένο σε reST.

Οι παράγραφοι δεν είναι τίποτε άλλο παρά κομμάτια κειμένου μέσα σε ένα έγγραφο, που ξεχωρίζουν από το υπόλοιπο κείμενο από μία ή περισσότερες κενές γραμμές, πριν και μετά από αυτές.

Με απλά λόγια, για να καταλάβει η reST ότι αυτό που εμείς γράφουμε είναι παράγραφος, μόλις την ολοκληρώσουμε, πατάμε δύο φορές :kbd:`enter` για να ξεκινήσουμε μία νέα. Πιο απλά, κάθε κομμάτι κειμένου θεωρείται παράγραφος όταν πριν και μετά από αυτό υπάρχουν κενές γραμμές. Αυτό ισχύει σε όλες τις markup γλώσσες.

Οι παράγραφοι πρέπει να είναι "στοιχισμένες" αριστερά δηλαδή να ξεκινάνε χωρίς :ref:`εσοχές <rest-concept-indentation-ref>` ως προς το επίπεδο που βρίσκονται. Αυτός ο απλός τρόπος σήμασνης (κενή γραμμή πριν και μετά, στοίχιση αριστερά) είναι ο τρόπος δημιουργίας μίας παραγράφου στη reST.

Μέσα σε μία παράγραφο μπορούμε να ενσωματώσουμε :ref:`σήμανση γραμμής <rest-concept-inline-markup-ref>`.

Το κείμενο που διαβάζετε σε αυτή την ενότητα γράφτηκε σκόπιμα σε έξι παραγράφους για να δείτε τον τρόπο δημιουργίας. Ο κώδικας που χρησιμοποιήθηκε φαίνεται στη συνέχεια::

   Η παράγραφος είναι το βασικό μπλοκ κειμένου σε ένα κείμενο
   γραμμένο σε reST.

   Οι παράγραφοι δεν είναι τίποτε άλλο παρά κομμάτια κειμένου μέσα
   σε ένα έγγραφο, που ξεχωρίζουν από το υπόλοιπο κείμενο από μία ή
   περισσότερες κενές γραμμές, πριν και μετά από αυτές.

   Με απλά λόγια, για να καταλάβει το reST ότι αυτό που εμείς
   γράφουμε, είναι παράγραφος, μόλις την ολοκληρώσουμε πατάμε δύο
   φορές enter για να ξεκινήσουμε μία νέα.  Πιο απλά, κάθε κομμάτι
   κειμένου θεωρείται παράγραφος όταν πριν και μετά από αυτό υπάρχουν
   κενές γραμμές. Αυτό ισχύει σε όλες τις markup γλώσσες.

   Οι παράγραφοι πρέπει να είναι "στοιχισμένες" αριστερά δηλαδή να
   ξεκινάνε χωρίς :ref:`εσοχές <rest-concept-indentation-ref>` ως
   προς το επίπεδο που βρίσκονται. Αυτός ο απλός τρόπος σήμασνης
   (κενή γραμμή πριν και μετά, στοίχιση αριστερά) είναι ο τρόπος
   δημιουργίας μίας παραγράφου στη reST.

   Μέσα σε μία παράγραφο μπορούμε να ενσωματώσουμε
   :ref:`σήμανση γραμμής <rest-concept-inline-markup-ref>`.

   Το κείμενο που διαβάζετε σε αυτή την ενότητα γράφτηκε σκόπιμα σε
   έξι παραγράφους για να δείτε τον τρόπο δημιουργίας. Ο κώδικας που
   χρησιμοποιήθηκε φαίνεται στη συνέχεια.

Παρατηρήστε ότι κάθε παράγραφος πρέπει να διαχωρίζεται με κενές γραμμές (στον κώδικα, αυτό που βλέπετε παραπάνω) για να διαμορφωθεί κατάλληλα στην έξοδο (στην html σελίδα [#]_, αυτό που βλέπετε τώρα).

.. [#] Ισχύει το ίδιο και για έξοδο pdf.


.. _rest-quotes-ref:

Αποσπάσματα (Quotes)
=======================



.. _rest-line-blocks-ref:

Ανεξάρτητες Γραμμές (Line Blocks)
======================================




.. _rest-literal-blocks-ref:

Μπλοκ Κυριολεκτικού Κειμένου (Literal Blocks)
================================================



.. _rest-hyperlinks-ref:

Υπερσύνδεσμοι (Hyperlinks)
=============================





.. _rest-lists-ref:

Λίστες (Lists)
=================

Οι λίστες είναι ειδικές κατασκευές μέσα σε ένα κείμενο, που χρησιμοποιούνται για παρουσιάσουν ταξινομημένα κάποια αντικείμενα (items). Τα αντικείμενα μπορεί να είναι κάποιοι απλοί όροι (όπως απλές λέξεις ή αριθμοί) έως ολόκληρες παράγραφοι, πίνακες, εικόνες ή ακόμη και άλλες λίστες (nested lists). Γενικά μία λίστα ξεχωρίζει από το υπόλοιπο κείμενο με κάποια ειδική διαμόρφωση (συνήθως με μία μικρή εσοχή). Επίσης, πριν από κάθε στοιχείο της λίστας προηγείται κάποιο σύμβολο (κουκίδα ή αριθμός ή κάποια λέξη).

Υπάρχουν διάφορες μορφές λίστας (θα τις δούμε στη συνέχεια) και κάθε μία χρησιμοποιείται για διαφορετικούς λόγους (αν και γενικά αυτό είναι υποκειμενικό). Ανεξάρτητα από το είδος και το λόγο χρήσης, θα πρέπει να έχετε υπόψη τα παρακάτω γενικά βασικά στοιχεία και κανόνες.

Απομόνωση
  Μία λίστα είναι ένα τυπογραφικό στοιχείο, θέλει το δικό της χώρο μέσα στο κείμενο. Θα πρέπει να διαχωρίζεται από το τρέχον κείμενο με κενές γραμμές. Να προσθέτετε πάντα μία (τουλάχιστο) κενή γραμμή πριν τη λίστα και μία (τουλάχιστο) μετά.

Αντικείμενα
  Οι λίστες αποτελούνται από αντικείμενα (items). Για παράδειγμα, η παράγραφος που διαβάζετε τώρα είναι το δεύτερο αντικείμενο μίας :ref:`λίστας ορισμών <rest-definition-list-ref>`. Η προηγούμενη ήταν το πρώτο και ακολουθούν και άλλα. Ένα αντικείμενο είναι κάτι που θέλουμε να αναδείξουμε στη λίστα (κείμενο, πίνακας, μία άλλη λίστα κ.λπ.).
  
  Η reST καταλαβαίνει τι είδους λίστα θέλουμε και πως να τη διαχειριστεί με βάση το πως **σηματοδοτούμε** (markup) τα αντικείμενα και τις **εσοχές** (identation) που χρησιμοποιούμε.

Σήμανση
  Πριν από κάθε αντικείμενο πρέπει να προηγείται μία σήμανση. Η σήμανση είναι είτε κάποιο σύμβολο (:ref:`λίστες κουκκίδας <rest-bullet-list-ref>`, :ref:`λίστες πεδίων <rest-field-list-ref>`, :ref:`λίστες επιλογών <rest-option-list-ref>`), είτε ένας αριθμός (:ref:`αριθμημένες λίστες <rest-enumerated-list-ref>`), είτε κάποια λέξη/φράση (:ref:`λίστα ορισμών <rest-definition-list-ref>`).
  
  Η σήμανση λέγεται *ενδείκτης* του αντικειμένου (item indicator). Ο ενδείκτης πρέπει να ξεκινάει χωρίς εσοχή ως προς το επίπεδο που ανήκει. Μετά τον ενδείκτη πρέπει να ακολουθεί *ένα* κενό και μετά το περιεχόμενο του αντικειμένου. Ο ενδείκτης σηματοδοτεί που ξεκινάει και τι είδους αντικείμενο είναι. Το κενό σηματοδοτεί που ξεκινάει το περιεχόμενο του αντικειμένου (με μία μικρή διαφοροποίηση στις :ref:`λίστες ορισμών <rest-definition-list-ref>`).

Εσοχές
  Όλα τα αντικείμενα *οποιασδήποτε λίστας* πρέπει να είναι απόλυτα στοιχισμένα μεταξύ τους. Αυτό σημαίνει ότι όλα πρέπει να έχουν την ίδια ακριβώς :ref:`εσοχή <rest-concept-indentation-ref>`, ως προς τη λίστα. Αν ενθέσουμε (nesting) μία λίστα μέσα σε μία άλλη, τα αντικείμενα της ένθετης πρέπει να έχουν εσοχές ως προς τη μητρική.

Κενός Χώρος
  Μία λίστα πρέπει να διαχωρίζεται από το υπόλοιπο κείμενο με (τουλάχιστο) μία γραμμή πριν και μία μετά τη λίστα. Τα αντικείμενα μίας λίστα μπορούν να διαχωρίζονται με κενές γραμμές αλλά αυτό είναι **προαιρετικό**. Ένθετο περιεχόμενο, όπως μία άλλη λίστα ή επιπλέον παράγραφοι, πρέπει να διαχωρίζονται με κενές γραμμές, αυτό είναι **υποχρεωτικό**.

Περιεχόμενο
  Μπορούμε να εισάγουμε αυθαίρετα οτιδήποτε περιεχόμενο, στα αντικείμενα μίας λίστας. Ανάλογα με το περιεχόμενο, ισχύουν τα εξής:

  #. Αν θέλουμε να αναπτύξουμε ένα αντικείμενο σε περισσότερες από μία παραγράφους, κάθε
     παράγραφος πρέπει να διαχωρίζεται από κενές γραμμές και να έχει την ίδια εσοχή με την προηγούμενη (αρχική).

  #. Το ίδιο ισχύει αν θέλουμε να εισάγουμε ειδικό υλικό όπως πίνακες, εικόνες, κώδικα κ.λπ.
     Ειδικό υλικό μπορούμε να εισάγουμε με κατάλληλες οδηγίες. Ακολουθήστε τις αντίστοιχες προδιαγραφές (θα τις δούμε στη συνέχεια ανάλογα με το περιεχόμενο).

  #. Μπορούμε να εισάγουμε μία νέα λίστα μέσα σε μία υπάρχουσα και μία νέα μέσα σε αυτή κ.ο.κ.
     Πρακτικά δεν υπάρχει περιορισμός στο επίπεδο ένθεσης (αλλά μην το παρακάνετε!). Επίσης επιτρέπονται όλοι οι συνδυασμοί ένθετων λιστών (unordered, ordered, definition κ.λπ.). Οι ένθετες λίστες (οποιουδήποτε επιπέδου) *πρέπει* να διαχωρίζονται με κενές γραμμές και να έχουν τις ανάλογες εσοχές. 

  .. note::
     Κάθε φορά που κάνετε ένθεση μίας νέας λίστας, οι στοιχίσεις θα πρέπει να προσαρμόζονται ανάλογα όλο και δεξιότερα. Αυτό ισχύει για οτιδήποτε υλικό προσθέσετε στην υπολίστα. Τηρήστε αυτές τις οδηγίες ευλαβικά για να έχετε τα αναμενόμενα αποτελέσματα.

Μορφοποίηση
  Οι λίστες εμφανίζονται με ιδιαίτερο τρόπο, σε σχέση με το υπόλοιπο κείμενο, στο έγγραφο εξόδου. Σε γενικές γραμμές, οι unordered και ordered λίστες θα εμφανιστούν με μία μικρή εσοχή ως προς το υπόλοιπο κείμενο και πιθανώς με μικρότερες ή μεγαλύτερες αποστάσεις μεταξύ παραγράφων. Στις unordered λίστες το κάθε αντικείμενο θα εμφανίζεται με μία κουκίδα (dot) ενώ στις ordered με τη μορφή αρίθμησης που θα επιλέξετε. Στις definition λίστες θα εμφανίζονται οι όροι σε μία γραμμή (πιθανώς με έντονη έμφαση, strong emphasis) και η επεξήγήσεις τους θα ακολουθούν στην επόμενη γραμμή.

.. note::

   Λάβετε υπόψη ότι η δημιουργία μίας λίστας (ο κώδικας) και το αποτέλεσμα (η μορφοποίηση), είναι δύο ανεξάρτητα αντικείμενα. Ο κώδικας είναι θέμα δικό σας (που και πως θα το συντάξετε) και της reST (που θα τον επεξεργαστεί) ενώ η εμφάνιση είναι θέμα του html επεξεργαστή, του browser που θα φιλοξενήσει την αντίστοιχη HTML σελίδα. Αν λοιπόν διαπιστώσετε ότι το αποτέλεσμα δεν είναι έτσι όπως το περιμένατε, ελέγτε αρχικά ότι ακολουθήσατε όλα τα παραπάνω και, αν και πάλι δε διορθωθεί το πρόβλημα, αναζητήστε βοήθεια στο διαδίκτυο, σχετική με θέμα της σελίδας εξόδου και τις ρυθμίσεις που απαιτούνται γιαυτή (κοιτάξτε για stylesheet, css κ.λπ.).

Στη συνέχεια περιγράφουμε τα είδη λιστών με τις ιδιαιτερότητες της κάθε μίας. Για κάθε μία, δίνουμε και ένα σύντομο παράδειγμα. Στο τέλος της ενότητας ακολουθεί ένα συγκεντρωτικό παράδειγμα μίας σύνθετης λίστας (κώδικας και αποτέλεσμα). Μπορείτε να αντιγράψετε το συγκεκριμένο κώδικα και να πειραματηστείτε με αυτόν. Στη reST μπορούμε να χρησιμοποιήσουμε τις εξής μορφές λιστών:

.. toctree::
   :maxdepth: 1

   rst-list-bullet
   rst-list-enumerated
   rst-list-definition
   rst-list-field
   rst-list-option



Πίνακες (Tables)
=================

dfjfh

.. toctree::
   :maxdepth: 1

   rst-tables


.. _rest-images-ref:

Εικόνες (Images)
===================





.. _rest-footnotes-ref:

Υποσημειώσεις (Footnotes)
=============================






.. _rest-citations-ref:

Παραπομπές (Citations)
===========================



.. _rest-admonitions-ref:

Προειδοποιήσεις (Admonitions)
===============================

Είναι ειδικά στοιχεία σώματος (τα γνωστά μηνύματα: "προσοχή", σημείωση", "πληροφορία" κ.λπ.) που μετά την επεξεργασία τους εμφανίζονται με τη μορφή πλαισίου, με συνήθως έγχρωμο υπόβαθρο (εξαρτάται από το επιλεγμένο θέμα ιστοσελίδας). Στο πλαίσιο εμφανίζεται ένας τίτλος είτε προκαθορισμένος (specific admonitions) είτε ορισμένος από εμάς (generic admonition) και στη συνέχεια κάποιο μήνυμα που ορίζεται από εμάς.

Μπορούμε να εισάγουμε admonitions σε οποιοδήποτε μέρος του εγγράφου. Τα ίδια τα admonitions μπορεί να περιλαμβάνουν αυθαίρετα άλλα στοιχεία σώματος. Όπως είπαμε, ο εμφανιζόμενος τίτλος εξαρτάται από τον τύπο του admonition.

Υπάρχουν δύο βασικοί τύποι: το γενικευμένο admonition και ειδικά τυποποιημένα.............



.. _rest-code-ref:

Κώδικας (Code)
=================



.. _rest-math-text-ref:

Μαθηματικό Κείμενο (Math Text)
================================



.. _rest-topics-ref:

Ανεξάρτητα Θέματα (Topics)
==============================



.. _rest-sidebars-ref:

Ανεξάρτητη Ενότητα (Sidebar)
================================




.. _rest-rubrics-ref:

Ρουμπρίκες (Rubrics)
=======================

Περίεργη έννοια έτσι; Προσωπικά ανακάλυψα τι είναι, μαθαίνοντας τη reST. Μπορείτε να κάνετε μία σχετική έρευνα στο δίκτυο για να μάθετε τι ακριβώς σημαίνει αυτός ο όρος.

Με λίγα λόγια, μία ρουμπρίκα είναι ένα σύστημα αξιολόγησης σπουδαστών. Για την ακρίβεια ένα σύστημα τεκμηρίωσης της αξιολόγησης (γιατί ένας μαθητής/σπουδαστής βαθμολογείται με 8 και ένας άλλος με 7,5;).

Στη reST ένα rubric απλά σημαίνει έναν τίτλο που εισάγεται όπου εμείς θέλουμε και δε λαμβάνεται υπόψη στον πίνακα περιεχομένων.



