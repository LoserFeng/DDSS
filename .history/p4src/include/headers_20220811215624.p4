/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/
#define CPU_REASON_CODE_SFLOW            0x4

const bit<16> TYPE_IPV4 = 0x800;
const bit<8>  TYPE_TCP  = 6;
const bit<8>  TYPE_UDP  = 17;
const bit<8>  IP_PROT_ICMP = 0x1;
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



// header dns_t {
//     bit<16> id;
//     bit<1>  qr;
//     bit<4>  opCode;
//     bit<1>  authAnswer;
//     bit<1>  trunc;
//     bit<1>  recurDesired;
//     bit<1>  recurAvail;
//     bit<3>  reserved;
//     bit<4>  respCode;
//     bit<16> qdCount;
//     bit<16> anCount;
//     bit<16> nsCount;
//     bit<16> arCount;
// }
// header dns_query1 {
//     bit<16> text;
// }

// header dns_query2 {
//     bit<24> text;
// }

// header dns_query3 {
//     bit<32> text;
// }

// header dns_query4 {
//     bit<40> text;
// }

// header dns_query8 {
//     bit<72> text;
// }


// header_union dnstext_t {
//     dns_query1 query1;
//     dns_query2 query2;
//     dns_query3 query3;
//     dns_query4 query4;
//     dns_query8 query8;
// }
// header dns_querylen_t {
//     bit<8>   totalLen;
// }
// header dnsqueryopt_t {
//     bit<16>  type;
//     bit<16>  class;
// }

// header dnsanswer_t {
//     bit<2>    compression;
//     bit<14>   offset;
//     bit<16>   type;
//     bit<16>   class;
//     bit<32>   ttl;
//     bit<16>   rdLength;
//     ip4Addr_t rdData;
// }


header icmp_t {
    bit<16> typeCode;
    bit<16> hdrChecksum;
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

    bit<1> is_dns;
    bit<1> is_query;
    bit<8> querylen;

}

struct headers {
    ethernet_t   ethernet;
    my_tunnel_t my_tunnel;
    ipv4_t       ipv4;
    tcp_t        tcp;
    dns_t                     dns;
    dns_querylen_t            dns_querylen;
    dnstext_t                 dns_querytext;
    dnsqueryopt_t             dns_queryopt;
    dnsanswer_t               dns_answer;
}



