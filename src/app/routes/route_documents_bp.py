from flask import Blueprint, render_template, request

documents_bp = Blueprint("documents", __name__, url_prefix="/documents")


@documents_bp.get("/new")
def new_document_form() -> str:
    return render_template(
        "docoments/new.html",
        page_title="Новый документ",
    )
