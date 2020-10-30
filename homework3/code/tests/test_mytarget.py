class TestMyTarget:
    def test_segment_creating(self, api_client, seg_name):
        api_client.create_segment(seg_name)
        assert api_client.find_segment_by_name(seg_name)

    def test_segment_deleting(self, api_client, seg_name):
        api_client.create_segment(seg_name)
        api_client.delete_segment_by_name(seg_name)
        assert not api_client.find_segment_by_name(seg_name)
