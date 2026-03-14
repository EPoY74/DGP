from flask import Blueprint, render_template, request

documents_bp = Blueprint("documents", __name__, url_prefix="/documents")


@documents_bp.get("/new")
def new_document_form() -> str:
    return render_template(
        "docoments/new.html",
        page_title="Новый документ",
    )


@documents_bp.post("/preview")
def preview_document() -> str:
    form_data = {
        "document_title": request.form.get("document_title", "").strip(),
        "document_number": request.form.get("document_number", "").strip(),
        "document_date": request.form.get("document_date", "").strip(),
        "site_name": request.form.get("site_name", "").strip(),
        "customer_name": request.form.get("customer_name", "").strip(),
        "note": request.form.get("note", "").strip(),
    }

    return render_template(
        "documents/preview.html",
        page_title="Просмотр документа",
        form_data=form_data,
    )
