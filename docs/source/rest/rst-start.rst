.. _rst-main-ref:

.. highlight:: rst

RestructuredText
####################


.. toctree::
   :maxdepth: 1
   :numbered:

   rst-basics
   rst-doc-structure
   rst-directives
   rst-roles
   rst-inline-markup
   rst-elements
   build-in-directives

https://docutils.readthedocs.io/en/sphinx-docs/ref/rst/restructuredtext.html

Η RestructuredText (συντ. RST ή ReST ή reST) είναι μία markup γλώσσα προγραμματισμού και παράλληλα ένα είδος format αρχείων κειμένου (αρχεία με κατάληξη ".rst"). Συγκαταλλέγεται στις "ελαφριές" γλώσσες σήμανσης (`lightweight markup languages <https://en.wikipedia.org/wiki/Lightweight_markup_language>`_) δηλαδή στις γλώσσες με απλή και διακριτική σύνταξη στις οποίες είναι εύκολη τόσο η γραφή όσο και η ανάγνωση του κειμένου από τον καθένα.

Δημιουργήθηκε από την κοινότητα προγραμματιστών Python (είναι μέρος του project "`Docutils <https://docutils.sourceforge.io/>`_"), προκειμένου να αποτελέσει ένα εύχρηστο εργαλείο παραγωγής τεχνικής τεκμηρίωσης, κώδικα Python. Το γεγονός αυτό όμως δε σημαίνει ότι δεν μπορεί να χρησιμοποιηθεί και σαν γενικής χρήσης markup γλώσσα. Αντίθετα, με τη reST μπορούμε εύκολα να δημιουργήσουμε κάθε μορφής κείμενο, από απλές αναφορές μέχρι και βιβλία.

Από το 2008 η reST έγινε μέρος του πυρήνα του συστήματος παραγωγής εγγράφων της Python, "Sphinx" και συνεπώς ο καλύτερος τρόπος για να τη χρησιμοποιήσει κανείς είναι μέσα από το συγκεκριμένο σύστημα. Στο παρόν βιβλίο μπορείτε να βρείτε ένα σύντομο οδηγό εγκατάστασης και χρήσης του συγκεκριμένου συστήματος.

Όπως με όλες τις markup γλώσσες, ο χρήστης έχει τη δυνατότητα δημιουργίας αρχείων απλού κειμένου (plain text files) σε οποιονδήποτε επεξεργαστή απλού κειμένου (plain text editor), σημαίνοντας κατάλληλα (marking up) τα σημεία εκείνα τα οποία θέλει να διαμορφώσει με ιδιαίτερο τρόπο. Για το σκοπό αυτό η reST παρέχει στο χρήστη κατάλληλους κανόνες σύνταξης για να προσαρμόσει τη διαμόρφωση του κειμένου στις ανάγκες του. Αυτούς τους κανόνες σύνταξης θα δούμε στη συνέχεια.

Η ονομασία "RestructuredText" (ναι είναι μία λέξη) επιλέχθηκε έτσι γιατί θεωρήθηκε ότι η συγκεκριμένη γλώσσα ήταν το αποτέλεσμα της *αναθεώρησης* (revision) και *επανερμηνείας* (reinterpretation) δύο άλλων γνωστών markup γλωσσών, της Setext_ και StructuredText_.

.. _Setext: https://en.wikipedia.org/wiki/Setext
.. _StructuredText: https://en.wikipedia.org/wiki/Structured_text

Μπορείτε να βρείτε ιστορικά στοιχεία καθώς και τους σκοπούς για τους οποίους δημιουργήθηκε η γλώσσα, στο κείμενο "`An Introduction to reStructuredText <https://docutils.sourceforge.io/docs/ref/rst/introduction.html>`_". Συγγραφέας του συγκεκριμένου κειμένου είναι ο ίδιος ο δημιουργός της γλώσσας `David Goodger <https://david.goodger.org/>`_. Επίσης μπορείτε να διαβάσετε τις προδιαγραφές της, γραμμένες από τον ίδιο, στο κείμενο "`reStructuredText Markup Specification <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`_". Το τελευταίο ήταν βασικός οδηγός για τη συγγραφή του οδηγού που διαβάζετε τώρα.




