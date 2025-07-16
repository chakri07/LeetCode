/*
 * Click `Run` to execute the snippet below!
 */

import java.io.*;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicReference;

/*
-> write-back cache -> we aret
-> froom write -> cache -> system

everything fits in cache

 */

class Event{
  String key;
  String value;


  public Event(String key, String value){
  this.key = key;
  this.value = value;
  }
}


class Store {  // java

  ConcurrentHashMap<String, String> valueMap = new ConcurrentHashMap<>();
  String persistentFileName = "PersistentStorage";

  // 
  AtomicReference<List<Event>> writeBuffer = new ArrayList<>();
  int write_idx = 0;

  File fileObj = File.open("persistentFileName");

  public write_to_disk(){
    while(true) {
      time.sleep(200);
      flieObj.flush(writeBuffer);

      while(true){
        if (writeBuffer.set(new ArrayList<>())) break;
      } 
    }
  }

  public write_to_disk_if_buffer_full(){
    while(true) {
      if len(writeBuffer) == 10{

      while(true){    
        flieObj.flush(writeBuffer);
        break;
      }

      while(true){
        if (writeBuffer.set(new ArrayList<>())) break;
      }
      }
    }
  }


  public void flush(){
    fileObj.write(writeBuffer[write_idx][0], writeBuffer[write_idx][1]);
    writeBuffer[write_idx][2].set(0);
    write_idx = (write_idx + 1) % 10; 
  }


  public Store() {
    // Called when the system first comes up. You can assume that no `get` or `put` calls will be made
    // before this function has completed. 
    
  }

  // lets say concurrent execution.

  public void put(String key, String value) {
    // Writes a given key/value pair into the store.  If `key` is already present replace the
    // current `value` with one given.  After this function returns, the value must be *durable*
    // meaning that even in the presence of failures (program crashing or power going out), subsequent
    // `get` calls for this key must continue to return the result of the most recent `put`.

    valueMap.put(key, value);
    // then write into file sytem 
    // fileObj.write(key + '->' + value,'a');
    // fileObj.flush();

    AtomicInteger atomicInteger = new AtomicInteger();
    atomicInteger.set(1);

    writeBuffer.put((key,value,atomicInteger));

    while(atomicInteger.get()!= 0){
      // do nothing
    }
    return 
  }

  public String get(String key) {
    // Returns the most recently `put` value for the given `key`.
    // Returns NULL, if no value has been `put` for this key.

    return valueMap.get(key);

  }
};














