/*************************************************************************
*********************** P A R S E R  *******************************
*************************************************************************/

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        transition parse_ethernet;
    }

    state parse_ethernet {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType){
            ETH_TYPE_MYTUNNEL: parse_my_tunnel;
            TYPE_IPV4:parse_ipv4;
            default: accept;
        }
    }
    state parse_my_tunnel {
        packet.extract(hdr.my_tunnel);
        transition select(hdr.my_tunnel.proto_id) {
            TYPE_IPV4: parse_ipv4;
            default: accept;
        }
    }

    state parse_ipv4 {
        packet.extract(hdr.ipv4);
        transition select(hdr.ipv4.protocol){
            TYPE_TCP : parse_tcp;
            default: accept;
        }
    }

    state parse_tcp {
        packet.extract(hdr.tcp);
        transition accept;
    }



#ifdef SFLOW_ENABLE
parser parse_fabric_sflow_header {
    extract(fabric_header_sflow);
    return parse_fabric_payload_header;
}
#endif


}

/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {

        //parsed headers have to be added again into the packet.


        packet.emit(hdr.ethernet);
        packet.emit(hdr.my_tunnel);
        packet.emit(hdr.ipv4);

        //Only emited if valid
        packet.emit(hdr.tcp);
    }
}
