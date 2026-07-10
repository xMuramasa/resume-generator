"""HTML -> PDF via headless Chrome."""
import subprocess


def html_to_pdf(html_path, pdf_path, chrome):
    subprocess.run(
        [str(chrome), "--headless", f"--print-to-pdf={pdf_path}",
         "--no-pdf-header-footer", html_path.resolve().as_uri()],
        check=True, capture_output=True,
    )
