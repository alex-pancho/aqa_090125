import xml.etree.ElementTree as ET
import logging.config


def find_data_in_xml(*, xml_file:str, group_id:int):
    """ Function accept 'xml' filename and group number. Output log with searched parameters, if exist """
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for group in root.findall('group'):
            group_number = group.find('number')
            if group_number is not None and group_number.text == str(group_id):
                timing_instance = group.find('timingExbytes')
                if timing_instance is not None:
                    data = timing_instance.find('incoming')
                    if data is not None:
                        xml_logger.info(f"Group {group_id}, timingExbytes/incoming: {data.text}")
                        return
        # Log message if search has no results
        xml_logger.info(f"Group {group_id}, No results")
    except FileNotFoundError as exc:
        xml_logger.error(f"{exc}")


logging.config.fileConfig('logger_config.ini')
xml_logger = logging.getLogger('xml_logger')

if __name__ == '__main__':
    for g_id in range(7):
        find_data_in_xml(xml_file='xml_files/groups.xml', group_id=g_id)