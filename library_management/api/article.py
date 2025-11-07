import frappe

@frappe.whitelist(allow_guest=True)
def get_articles():
    articles = frappe.get_all(
        "Article",
        fields=["article_name", "author", "publisher"]
    )
    return articles
