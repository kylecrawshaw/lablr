import qrcode as _qrcode


def get_qrcode(url, size=200, border=2):
    # Generate a QRCode
    qr = _qrcode.QRCode(
        version=1,
        error_correction=_qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image()


    # Resize the QR image to fit with
    qr_w = size - int(size * 0.13)
    qr_size = (qr_w, qr_w)

    return qr_img._img.resize(qr_size)
