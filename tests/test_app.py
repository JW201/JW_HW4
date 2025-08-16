from pathlib import Path
import tempfile, shutil, re
import app

def test_make_output_file():
    tmp = Path(tempfile.mkdtemp())
    try:
        p = app.make_output_file("junyi", tmp)
        assert p.exists()
        assert p.parent == tmp
        assert p.read_text(encoding="utf-8").startswith("Hello from junyi")
        assert re.match(r"hello_junyi_\d{8}-\d{6}\.txt$", p.name)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
