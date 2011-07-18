# You can found this information in
# http://www.adobe.com/devnet/acrobat/pdfs/PDF32000_2008.pdf document at page
# number 61

# (Security handlers of revision 2) Print the document. (Security handlers of
# revision 3 or greater) Print the document (possibly not at the highest quality
# level, depending on whether bit 12 is also set).
print_document                      = int("000000000100", 2) # bit 3

# Modify the contents of the document by operations other than those controlled
# by bits 6, 9, and 11.
modify_document                     = int("000000001000", 2) # bit 4

# (Security handlers of revision 2) Copy or otherwise extract text and graphics
# from the document, including extracting text and graphics (in support of
# accessibility to users with disabilities or for other purposes).
# (Security handlers of revision 3 or greater) Copy or otherwise extract text
# and graphics from the document by operations other than that controlled by bit
# 10.
copy_text_and_graphics              = int("000000010000", 2) # bit 5

# Add or modify text annotations, fill in interactive form fields, and, if bit 4
# is also set, create or modify interactive form fields (including signature
# fields).
add_or_modify_text_annotations_and_fill_form_fields = int("100000", 2) # bit 6

# (Security handlers of revision 3 or greater) Extract text and graphics (in
# support of accessibility to users with disabilities or for other purposes).
content_copying_for_accessibility   = int("01000000000", 2) # bit 10

# (Security handlers of revision 3 or greater) Assemble the document (insert,
# rotate, or delete pages and create bookmarks or thumbnail images), even if bit
# 4 is clear.
assemble_insert_rotate_delete_page  = int("010000000000", 2) # bit 11

# (Security handlers of revision 3 or greater) Print the document to a
# representation from which a faithful digital copy of the PDF content could be
# generated. When this bit is clear (and bit 3 is set), printing is limited to a
# low-level representation of the appearance, possibly of degraded quality.
high_quality_document_printing = int("0100000000000", 2) # bit 12
