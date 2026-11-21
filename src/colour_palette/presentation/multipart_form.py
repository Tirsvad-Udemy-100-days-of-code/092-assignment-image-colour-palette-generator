"""!
@file multipart_form.py
@brief Read a multipart/form-data request body with the standard library.
"""

from dataclasses import dataclass
from email.parser import BytesParser
from email.policy import HTTP


@dataclass(frozen=True)
class FormField:
    """!
    @brief One field of a submitted form.
    """

    ## Field name from the form.
    name: str
    ## Raw value of the field.
    data: bytes
    ## File name for a file field, else None.
    filename: str | None = None
    ## Content type sent by the browser.
    content_type: str = "text/plain"


class FormParseError(ValueError):
    """!
    @brief Raised when a request body is not a valid multipart form.
    """


def parse_multipart_form(body: bytes, content_type: str) -> dict[str, FormField]:
    """!
    @brief Split a multipart/form-data body into its fields.
    @param body The raw request body.
    @param content_type The Content-Type header, including the boundary.
    @return The fields by name; the last one wins when a name repeats.
    @throws FormParseError When the content type is not multipart/form-data.
    """
    if not content_type.lower().startswith("multipart/form-data"):
        raise FormParseError("Expected a multipart/form-data upload")
    header = f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode("latin-1")
    message = BytesParser(policy=HTTP).parsebytes(header + body)
    if not message.is_multipart():
        raise FormParseError("The upload has no form fields")

    fields: dict[str, FormField] = {}
    for part in message.iter_parts():
        name = part.get_param("name", header="content-disposition")
        if not isinstance(name, str):
            continue
        payload = part.get_payload(decode=True)
        fields[name] = FormField(
            name=name,
            data=payload if isinstance(payload, bytes) else b"",
            filename=part.get_filename(),
            content_type=part.get_content_type(),
        )
    return fields
