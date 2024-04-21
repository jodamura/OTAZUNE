import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardActions from '@mui/material/CardActions';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField'; 
import SendIcon from '@mui/icons-material/Send';

function App() {
  const [requestdata, setRequestData] = useState([]);
  const [dataLength, setDataLength] = useState(0); 
  const [selectedTour, setSelectedTour] = useState(null);
  const [open, setOpen] = useState(false);
  const [openpost, setOpenPost] = useState(false);
  const [proposalText, setProposalText] = useState('');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/');
        setRequestData(response.data);
        setDataLength(response.data.length);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    fetchData();
  }, []);

  const handleOpen = (tour) => {
    setSelectedTour(tour);
    setOpen(true);
  };

  const handleOpenPost = (tour) => {
    setSelectedTour(tour);
    setOpenPost(true);
  };

  const handleClose = () => {
    setOpen(false);
    setOpenPost(false);
  };

  // 提案用テキストエリアの変更を処理する関数
  const handleProposalChange = (event) => {
    setProposalText(event.target.value);
  };

  return (
      <div className='container-fluid'>
        <h3>現在募集中の案件:{dataLength}件</h3>
        <div className='cardlist'>
          {requestdata.map((tour) => (
            <div key={tour.ID} className='cardelem'>
              <Card sx={{ minWidth: 350, minHeight: 250 }}>
                <CardContent>
                <Typography variant="h6" component="div" sx={{ fontWeight: 'bold', overflow: 'hidden', textOverflow: 'ellipsis', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical' }}>
                  {tour.Requests ? tour.Requests : "No-requests"}
                </Typography>
                  <Typography sx={{ mb: 1.5 }} color="text.secondary" gutterBottom>
                    依頼者：{tour.CustomerName}
                  </Typography>
                  <Typography variant="body2">
                    国籍：{tour.Country}
                    <br />
                    <br />
                    予約登録日: {tour.RequestedDate}
                  </Typography>
                </CardContent>
                <CardActions>
                  <Button size="small" variant="contained" color="success" onClick={() => handleOpen(tour)}>詳細を見る</Button>
                  <Button size="small" variant="contained" onClick={() => handleOpenPost(tour)}>提案ページへ</Button>
                </CardActions>
              </Card>
            </div>
          ))}
          <Modal
            open={open}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
          >
            <Box
              sx={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                width: '50%',
                bgcolor: 'background.paper',
                borderRadius: '5px',
                boxShadow: 24,
                p: 4,
                color: '#363636'
              }}
            >
              {selectedTour && (
                <>
                  <Typography id="modal-modal-title" variant="h6" component="h2" sx={{ fontWeight: 'bold' }} >
                    {selectedTour.Requests}
                  </Typography>
                  <Typography id="modal-modal-description" sx={{ mt: 2 }}>
                    依頼者：{selectedTour.CustomerName}
                    <br />
                    国籍：{selectedTour.Country}
                    <br />
                    e-メール：{selectedTour.Email}
                    <br />
                    電話番号：{selectedTour.PhoneNumber}
                    <br />
                    生年月日：{selectedTour.BirthDate}
                    <br />
                    大人{selectedTour.AdultParticipants}名
                    <br />
                    <br />
                    予約登録日: {selectedTour.RequestedDate}
                  </Typography>
                </>
              )}
            </Box>
          </Modal>
          <Modal
            open={openpost}
            onClose={handleClose}
            aria-labelledby="modal-modal-title"
            aria-describedby="modal-modal-description"
          >
            <Box
              sx={{
                position: 'absolute',
                top: '50%',
                left: '50%',
                transform: 'translate(-50%, -50%)',
                width: '50%',
                bgcolor: 'background.paper',
                borderRadius: '5px',
                boxShadow: 24,
                p: 4,
                color: '#363636'
              }}
            >
              {selectedTour && (
                <>
                  <Typography sx={{mb: 2}} id="modal-modal-title" variant="h6" component="h2">
                    提案ページ
                  </Typography>
                  <Typography sx={{mb: 1.5}}>
                    <TextField
                      required
                      id="standard-required"
                      label="お名前"
                      defaultValue=""
                      variant="standard"
                    />
                  </Typography>
                  <Typography sx={{mb: 3}}>
                    <TextField
                      required
                      id="standard-required"
                      label="メールアドレス"
                      defaultValue=""
                      variant="standard"
                    />
                  </Typography>
                  <Typography id="modal-modal-description" sx={{ mb: 2 }}>
                    <TextField
                      required
                      id="standard-multiline-flexible"
                      label="提案内容"
                      multiline
                      maxRows={8}
                      fullWidth
                      value={proposalText}
                      onChange={handleProposalChange}
                      variant="standard"
                    />
                  </Typography>
                  <CardActions>
                    <Button size="small" variant="contained" endIcon={<SendIcon />}>提案する</Button>
                  </CardActions>
                </>
              )}
            </Box>
          </Modal>
        </div>
      </div>
  );
}

export default App;
