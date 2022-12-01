import click
from flaskblog.routes import get_all_items, get_one_item_by_id, create_new_item, update_one_item_by_id, delete_one_item_by_id, post_in_db

message_global = 'Item by default'

@click.command
@click.option('--get', default=0, help='0 = get all; 1 = get by id (need id)')
@click.option('--id', default=1349784310, help='id of the item to get')
@click.option('--post', default=0, help='0 = no create new item (default). 1 = create new item (need message) ')
@click.option('--message', default=message_global, help='message of the new item')
@click.option('--patch', default=0, help='0 = no update item. 1 = update item (need id)')
@click.option('--delete', default=0, help='0 = no delete item. 1 = delete item (need id)')
@click.option('--getreport', default=0, help='0 = get all; 1 = get by id (need id)')
def cli(get,id,post,message,patch,delete, getreport):
    if get==1:
        item = get_one_item_by_id(id)
        print(item)
    elif  post==1:
        item = create_new_item(message)
        print(item)
    elif patch==1:
        item = update_one_item_by_id(id)
        print(item)
    elif delete==1:
        item = delete_one_item_by_id(id)
        print(item)
    elif getreport==1:
        item = post_in_db()
        print(item)
    else: 
        item = get_all_items()
        print(item)
    return None

if __name__ == '__main__':
    cli()