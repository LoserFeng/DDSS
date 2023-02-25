/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

const bit<16> TYPE_IPV4 = 0x800;
const bit<8>  TYPE_TCP  = 6;
const bit<8>  TYPE_UDP  = 17;
// const bit<9>  SYN_FLAG  = 1;
const bit<16> ETH_TYPE_MYTUNNEL = 0x1212;
#define BLOOM_FILTER_ENTRIES 4096
#define BLOOM_FILTER_BIT_WIDTH 32
#define PACKET_THRESHOLD 100
#define PACKET_MIN_THRESHOLD 20
#define BLOOM_FILTER_ENTRIES2 4096


typedef bit<9> port_t;
typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;


header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

header my_tunnel_t {
    bit<16> proto_id;
    bit<32> tun_id;
    bit<1> checked;
    bit<7> sid;
    bit<8> _pad;
    ip4Addr_t srcAddr;
    ip4Addr_t dstAddr;
}

header ipv4_t {
    bit<4>    version;
    bit<4>    ihl;
  //  bit<6>    dscp;
   // bit<2>    ecn;
    bit<8>    tos;
    bit<16>   totalLen;
    bit<16>   identification;
    bit<3>    flags;
    bit<13>   fragOffset;
    bit<8>    ttl;
    bit<8>    protocol;
    bit<16>   hdrChecksum;
    ip4Addr_t src_addr;
    ip4Addr_t dst_addr;
}



header tcp_t{
    bit<16> srcPort;
    bit<16> dstPort;
    bit<32> seqNo;
    bit<32> ackNo;
    bit<4>  dataOffset;
    bit<4>  res;
    bit<1>  cwr;
    bit<1>  ece;
    bit<1>  urg;
    bit<1>  ack;
    bit<1>  psh;
    bit<1>  rst;
    bit<1>  syn;
    bit<1>  fin;
    bit<16> window;
    bit<16> checksum;
    bit<16> urgentPtr;
}

header sflow_hdr_t {

        bit<32>version;
        bit<32>addrType;
        bit<32>ipAddress ;
        bit<32>subAgentId ;
        bit<32>seqNumber ;
        bit<32>uptime ;
        bit<32>numSamples ;
    
}

header sflow_sample_t {

    bit<20>enterprise ;
    bit<12>format ;
    bit<32>sampleLength;
    bit<32>seqNumer ;
    bit<8>srcIdType  ;
    bit<24>srcIdIndex;
    bit<32>samplingRate;
    bit<32>samplePool;
    bit<32>numDrops ;
    bit<32>inputIfindex ;
    bit<32>outputIfindex ;
    bit<32>numFlowRecords;

}

header_type sflow_raw_hdr_record_t {
    // this header is attached to each pkt sample (flow_record)

    bit<20>enterprise  ;
    bit<12>format ;
    bit<32>flowDataLength ;
    bit<32>headerProtocol ;
    bit<32>frameLength;
    bit<32>bytesRemoved;
    bit<32>headerSize ;

}


header_type sflow_sample_cpu_t {
    fields {
        sampleLength        : 16;
        samplePool          : 32;
        inputIfindex        : 16;
        outputIfindex       : 16;
        numFlowRecords      : 8;
        sflow_session_id    : 3;
        pipe_id             : 2;
    }
}



























struct metadata {
    bit<14> ecmp_hash;
    bit<14> ecmp_group_id;
    bit<1>  syn_defence_flag;
    bit<14> a;
    bit<32> output_hash_one;
    bit<32> output_hash_two;
    bit<32> counter_one;
    bit<32> counter_two;
    bit<32> output_hash_three;
    bit<32> counter_three;
    bit<32> output_hash_four;
    bit<32> counter_four;
    bit<1> is_to_clean;
    bit<14> ng_hash;
    bit<48>  loc_mac;

}

struct headers {
    ethernet_t   ethernet;
    my_tunnel_t my_tunnel;
    ipv4_t       ipv4;
    tcp_t        tcp;
}



