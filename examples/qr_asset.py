from lablr import Region, SingleItemRegion, TextItem, ImageItem
from lablr.helpers import get_qrcode


def qr_label(output_path, qr_data, logo_path, asset_id, title='Property Of',
             subtitle='A Company', font_size=18, bg_color=(255, 255, 255)):
    label = Region('label', size=(350, 200))

    split_region_width = label.size.width/2
    split_region_height = label.size.height

    qr_region = SingleItemRegion(
        'qr_region',
        ImageItem(get_qrcode(qr_data), 'qrcode', bg_color=bg_color),
        align='center',
        vertical_align='middle',
        size=(split_region_width, int(split_region_height*0.87)),
        fit=True,
        bg_color=bg_color,
        x_offset=5,
    )

    asset_region = SingleItemRegion(
        'asset_id_region',
        TextItem(asset_id, 'asset_id', font_size=font_size, bg_color=bg_color),
        align='center',
        vertical_align='top',
        size=(split_region_width, int(split_region_height*0.2)),
        position=qr_region.position_below,
        bg_color=bg_color,
        y_offset=-10,
    )

    title_region = SingleItemRegion(
        'title_region',
        TextItem(title, 'title', font_size=font_size, bg_color=bg_color),
        align='center',
        vertical_align='bottom',
        size=(split_region_width, int(split_region_height*0.2)),
        bg_color=bg_color,
        position=qr_region.position_right,
        y_offset=10
    )

    logo = ImageItem(logo_path, 'logo', bg_color=bg_color)
    logo.resize(0.5)
    logo_region = SingleItemRegion(
        'logo_region',
        logo,
        align='center',
        size=(split_region_width, int(split_region_height*0.5)),
        position=title_region.position_below,
        bg_color=bg_color,
        y_offset=20,
    )

    subtitle_region = SingleItemRegion(
        'company_region',
        TextItem(subtitle, 'subtitle', font_size=font_size, bg_color=bg_color),
        align='center',
        vertical_align='top',
        size=(split_region_width, int(split_region_height*0.2)),
        position=logo_region.position_below,
        bg_color=bg_color,
    )
    

    label.add_item(qr_region)
    label.add_item(asset_region)
    label.add_item(title_region)
    label.add_item(logo_region)
    label.add_item(subtitle_region)

    label.save(output_path)
    return label

