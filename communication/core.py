import logging


class Core:
    def __init__(self):
        self.__topics = {}

    def topic_list(self):
        return list(self.__topics.keys())

    def __create_topic(self, topic):
        self.__topics[topic] = None

    def push_message(self, topic, msg):
        if topic not in self.__topics:
            logging.warning("Topic %topic doesn't exist. Creating new topic")
            self.__create_topic(topic)
        self.__topics[topic] = msg

    def get_message(self, topic):
        result = None
        if topic in self.__topics:
            result = self.__topics[topic]
        else:
            logging.error("Unknown")
        return result
