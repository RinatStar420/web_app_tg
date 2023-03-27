from scrap_tgstat_page import parser, db
from .. import models




def save_in_core_channel():
    db_obj = db()
    url = db_obj.tgstat_link()
    id_channel = db_obj.get_last_id()
    obj = parser()
    obj.write_tgstat_to_html(url_channel=url)
    channel = models.Channel.objects.get(id=id_channel)
    channel.ERR = obj.scrap_err_channel()
    channel.save(update_fields=["ERR"])
    channel.CPM = obj.scrap_cpm_channel()
    channel.save(update_fields=["CPM"])
    channel.subscribes_count = obj.scrap_subscribes_count_channel()
    channel.save(update_fields=["subscribes_count"])
    channel.coverage = obj.scrap_coverage_channel()
    channel.save(update_fields=["coverage"])





