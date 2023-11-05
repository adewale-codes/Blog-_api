def paginate_items(items, page, per_page):
    total_items = len(items)
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    items_on_page = items[start_idx:end_idx]
    total_pages = (total_items + per_page - 1) // per_page

    return items_on_page, total_pages
