#!/usr/bin/python

# Copyright KOLIBERO under one or more contributor license agreements.  
# KOLIBERO licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import time
import os
import uuid
import argparse
from datetime import datetime
from kafka import KafkaConsumer, SimpleConsumer
from elasticsearch import Elasticsearch

def save():
  print "save"

  # Kafka
  consumer = KafkaConsumer(bootstrap_servers=args.kafka_bootstrap_srvs, group_id=args.kafka_group_id)
  consumer.subscribe([args.kafka_source_topic])

  # Elastic
  es = Elasticsearch(args.elastic_url)

  for msg in consumer:
    #
    indata = json.loads(msg.value)
    #print indata
    #
    #today = str(datetime.today())[0:10]
    #
    #print today
    #
    myid = str(uuid.uuid4())
    #
    es.index(index=args.elastic_index,doc_type=args.elastic_doc_type,id=myid, body=indata)


if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Backup topic")
  parser.add_argument('--kafka_bootstrap_srvs', default="localhost:9092")
  parser.add_argument('--kafka_group_id', default="backup_topic")
  parser.add_argument('--kafka_source_topic', default="btc_rates2")
  parser.add_argument('--elastic_url', default="localhost:9200")
  parser.add_argument('--elastic_index', default="good")
  parser.add_argument('--elastic_doc_type', default="good")

  #parser.add_argument('--target_file', default="btc_rates2")
  #
  args = parser.parse_args()
  #
  save()
