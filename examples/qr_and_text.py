from lablr import Region, SingleItemRegion, TextItem, ImageItem
from lablr.helpers import get_qrcode


def qr_and_text(output_path, qr_data, label_text, font_size=35, bg_color=(255, 255, 255)):
    label = Region('label', size=(300, 350), bg_color=bg_color)

    qr_region = SingleItemRegion(
        'qr_region',
        ImageItem(get_qrcode(qr_data, size=label.size.width), 'qrcode', bg_color=bg_color),
        align='center',
        vertical_align='bottom',
        size=(label.size.width, int(label.size.height*0.8)),
        bg_color=bg_color,
    )

    asset_region = SingleItemRegion(
        'asset_id_region',
        TextItem(label_text, 'asset_id', font_size=font_size, bg_color=bg_color),
        align='center',
        vertical_align='top',
        size=(label.size.width, int(label.size.height*0.2)),
        position=qr_region.position_below,
        bg_color=bg_color,
        y_offset=15
    )

    label.add_item(qr_region)
    label.add_item(asset_region)

    label.save(output_path)
    return label